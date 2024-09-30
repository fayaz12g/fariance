package one.fayaz.fariance.blocks;

import net.minecraft.core.Direction;
import net.minecraft.core.particles.ParticleOptions;
import net.minecraft.core.particles.SimpleParticleType;
import net.minecraft.world.item.context.BlockPlaceContext;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.TorchBlock;
import net.minecraft.world.level.block.WallTorchBlock;
import net.minecraft.world.level.block.state.BlockState;

public class CustomTorchBlock extends TorchBlock {
    private final Block wallTorch;

    public CustomTorchBlock(ParticleOptions particleType, Properties properties, Block wallTorch) {
        super((SimpleParticleType) particleType, properties);
        this.wallTorch = wallTorch;
    }

    @Override
    public BlockState getStateForPlacement(BlockPlaceContext context) {
        BlockState state = super.getStateForPlacement(context);
        Direction direction = context.getClickedFace();

        if (direction != Direction.DOWN && direction != Direction.UP) {
            return this.wallTorch.defaultBlockState().setValue(WallTorchBlock.FACING, direction);
        }

        return state;
    }
}