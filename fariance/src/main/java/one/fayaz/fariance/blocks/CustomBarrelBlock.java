package one.fayaz.fariance.blocks;

import net.minecraft.core.BlockPos;
import net.minecraft.core.Direction;
import net.minecraft.core.NonNullList;
import net.minecraft.network.chat.Component;
import net.minecraft.sounds.SoundEvent;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.sounds.SoundSource;
import net.minecraft.stats.Stats;
import net.minecraft.world.*;
import net.minecraft.world.entity.player.Inventory;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.inventory.AbstractContainerMenu;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.EntityBlock;
import net.minecraft.world.level.block.entity.BlockEntity;
import net.minecraft.world.level.block.entity.BlockEntityType;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.block.state.StateDefinition;
import net.minecraft.world.level.block.state.properties.BlockStateProperties;
import net.minecraft.world.level.block.state.properties.BooleanProperty;
import net.minecraft.world.level.block.state.properties.DirectionProperty;
import net.minecraft.world.phys.BlockHitResult;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import one.fayaz.fariance.FarianceMod;
import one.fayaz.fariance.ItemRegistry;

import javax.annotation.Nullable;

public class CustomBarrelBlock extends Block implements EntityBlock {
    public static final DirectionProperty FACING = BlockStateProperties.FACING;
    public static final BooleanProperty OPEN = BlockStateProperties.OPEN;

    public static final DeferredRegister<BlockEntityType<?>> BLOCK_ENTITIES = DeferredRegister.create(ForgeRegistries.BLOCK_ENTITY_TYPES, FarianceMod.MODID);

    public static RegistryObject<BlockEntityType<CustomBarrelBlockEntity>> CUSTOM_BARREL_BLOCK_ENTITY;

    public CustomBarrelBlock(BlockBehaviour.Properties properties) {
        super(properties);
        this.registerDefaultState(this.stateDefinition.any().setValue(FACING, Direction.NORTH).setValue(OPEN, Boolean.FALSE));
    }

    public InteractionResult use(BlockState state, Level level, BlockPos pos, Player player, InteractionHand hand, BlockHitResult hit) {
        if (level.isClientSide) {
            return InteractionResult.SUCCESS;
        } else {
            BlockEntity blockEntity = level.getBlockEntity(pos);
            if (blockEntity instanceof CustomBarrelBlockEntity) {
                player.openMenu((MenuProvider) blockEntity);
                player.awardStat(Stats.OPEN_BARREL);
            }
            return InteractionResult.CONSUME;
        }
    }

    @Override
    public void onRemove(BlockState state, Level level, BlockPos pos, BlockState newState, boolean isMoving) {
        if (!state.is(newState.getBlock())) {
            BlockEntity blockEntity = level.getBlockEntity(pos);
            if (blockEntity instanceof CustomBarrelBlockEntity) {
                Containers.dropContents(level, pos, (CustomBarrelBlockEntity) blockEntity);
                level.updateNeighbourForOutputSignal(pos, this);
            }
            super.onRemove(state, level, pos, newState, isMoving);
        }
    }

    public static void setOpen(Level level, BlockPos pos, BlockState state, boolean open) {
        level.setBlock(pos, state.setValue(OPEN, open), 3);
        playSound(level, pos, open);
    }

    private static void playSound(Level level, BlockPos pos, boolean open) {
        double d0 = (double)pos.getX() + 0.5D;
        double d1 = (double)pos.getY() + 0.5D;
        double d2 = (double)pos.getZ() + 0.5D;
        SoundEvent soundEvent = open ? SoundEvents.BARREL_OPEN : SoundEvents.BARREL_CLOSE;
        level.playSound(null, d0, d1, d2, soundEvent, SoundSource.BLOCKS, 0.5F, level.random.nextFloat() * 0.1F + 0.9F);
    }

    @Override
    protected void createBlockStateDefinition(StateDefinition.Builder<Block, BlockState> builder) {
        builder.add(FACING, OPEN);
    }

    @Nullable
    @Override
    public BlockEntity newBlockEntity(BlockPos pos, BlockState state) {
        return new CustomBarrelBlockEntity(pos, state);
    }

    public static void registerBlockEntities() {
        CUSTOM_BARREL_BLOCK_ENTITY = BLOCK_ENTITIES.register(
                "custom_barrel",
                () -> BlockEntityType.Builder.of(CustomBarrelBlockEntity::new,
                        ItemRegistry.GENERATED_BLOCKS.values().stream()
                                .filter(block -> block.get() instanceof CustomBarrelBlock)
                                .map(RegistryObject::get)
                                .toArray(CustomBarrelBlock[]::new)
                ).build(null)
        );

        BLOCK_ENTITIES.register(FMLJavaModLoadingContext.get().getModEventBus());
    }

    // Add other necessary methods like use, onRemove, etc.
}

class CustomBarrelBlockEntity extends BlockEntity implements WorldlyContainer, MenuProvider  {
    private NonNullList<ItemStack> items = NonNullList.withSize(27, ItemStack.EMPTY);

    public CustomBarrelBlockEntity(BlockPos pos, BlockState state) {
        super(CustomBarrelBlock.CUSTOM_BARREL_BLOCK_ENTITY.get(), pos, state);
    }

    @Override
    public int[] getSlotsForFace(Direction side) {
        return new int[27]; // Allow access from all sides
    }

    @Override
    public boolean canPlaceItemThroughFace(int index, ItemStack itemStackIn, @Nullable Direction direction) {
        return true; // Allow placing items from all sides
    }

    @Override
    public boolean canTakeItemThroughFace(int index, ItemStack stack, Direction direction) {
        return true; // Allow taking items from all sides
    }

    @Override
    public int getContainerSize() {
        return 27;
    }

    @Override
    public boolean isEmpty() {
        return this.items.stream().allMatch(ItemStack::isEmpty);
    }

    @Override
    public ItemStack getItem(int index) {
        return this.items.get(index);
    }

    @Override
    public ItemStack removeItem(int index, int count) {
        return ContainerHelper.removeItem(this.items, index, count);
    }

    @Override
    public ItemStack removeItemNoUpdate(int index) {
        return ContainerHelper.takeItem(this.items, index);
    }

    @Override
    public void setItem(int index, ItemStack stack) {
        this.items.set(index, stack);
        if (stack.getCount() > this.getMaxStackSize()) {
            stack.setCount(this.getMaxStackSize());
        }
    }

    @Override
    public boolean stillValid(Player player) {
        return Container.stillValidBlockEntity(this, player);
    }

    @Override
    public void clearContent() {
        this.items.clear();
    }


    @Override
    public AbstractContainerMenu createMenu(int windowId, Inventory playerInventory, Player player) {
        return new CustomBarrelMenu(windowId, playerInventory, this);
    }

    @Override
    public Component getDisplayName() {
        return Component.translatable("container.barrel");
    }

    @Override
    public void startOpen(Player player) {
        if (!this.remove && !player.isSpectator()) {
            CustomBarrelBlock.setOpen(this.level, this.worldPosition, this.getBlockState(), true);
        }
    }

    @Override
    public void stopOpen(Player player) {
        if (!this.remove && !player.isSpectator()) {
            CustomBarrelBlock.setOpen(this.level, this.worldPosition, this.getBlockState(), false);
        }
    }

    // Add methods for saving and loading NBT data
}