package one.fayaz.fariance.blocks;

import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.state.BlockBehaviour;
import org.jetbrains.annotations.NotNull;
import net.minecraft.core.Direction;
import net.minecraft.world.item.context.BlockPlaceContext;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.RedstoneTorchBlock;
import net.minecraft.world.level.block.RedstoneWallTorchBlock;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.block.state.BlockState;


public class CustomRedstoneTorchBlock extends RedstoneTorchBlock {
    private final Block wallTorch;

    public CustomRedstoneTorchBlock(Properties properties, Block wallTorch) {
        super(properties);
        this.wallTorch = wallTorch;
    }

    @Override
    public BlockState getStateForPlacement(BlockPlaceContext context) {
        BlockState state = super.getStateForPlacement(context);
        Direction direction = context.getClickedFace();

        if (direction != Direction.DOWN && direction != Direction.UP) {
            return this.wallTorch.defaultBlockState()
                    .setValue(RedstoneWallTorchBlock.FACING, direction)
                    .setValue(RedstoneWallTorchBlock.LIT, state.getValue(LIT));
        }

        return state;
    }
}